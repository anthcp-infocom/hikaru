from hikaru import * 

x = Pod(apiVersion='v1', kind='Pod',
        metadata=ObjectMeta(name='hello-kiamol-3'),
        spec=PodSpec(
            containers=[Container(name='web', image='kiamol/ch02-hello-kiamol') ]
             )
    )

print(get_yaml(x))

with open("examples/pod.yaml", "w") as text_file:
    text_file.write(get_yaml(x))

docs = load_full_yaml(path="examples/pod.yaml")
print(get_python_source(docs[0], assign_to='x', style="black"))

docs = load_full_yaml(path="examples/route.yaml")
print(get_python_source(docs[0], assign_to='x', style="black"))

y = Route(
    spec=RouteSpec(
        to=RouteTargetReference(kind="Service", name="service-name"),
        host="www.example.com",
        path="/test",
    ),
    apiVersion="v1",
    kind="Route",
    metadata=ObjectMeta(name="route-unsecured"),
)

print(get_yaml(y))

docs = load_full_yaml(path="examples/StatefullSet.yaml")
print(get_python_source(docs[0], assign_to='x', style="black"))

z = StatefulSet(
    apiVersion="apps/v1",
    kind="StatefulSet",
    metadata=ObjectMeta(name="my-set", labels={"name": "my-set"}),
    spec=StatefulSetSpec(
        selector=LabelSelector(matchLabels={"name": "my-set"}),
        serviceName="my-set-svc",
        template=PodTemplateSpec(
            metadata=ObjectMeta(labels={"name": "my-set"}),
            spec=PodSpec(
                containers=[
                    Container(
                        name="my-set",
                        image="alpine:latest",
                        imagePullPolicy="Always",
                        args=[
                            'echo "Starting statefulset pod"; cat /etc/app/conf/set.conf; while true; do sleep 600; done'
                        ],
                        command=["/bin/sh", "-c"],
                        volumeMounts=[
                            VolumeMount(mountPath="/etc/app/conf", name="conf-vol")
                        ],
                    )
                ],
                initContainers=[
                    Container(
                        name="init-set",
                        image="alpine:latest",
                        command=["/mnt/scripts/run.sh"],
                        volumeMounts=[
                            VolumeMount(mountPath="/mnt/scripts", name="scripts-vol"),
                            VolumeMount(mountPath="/mnt/data", name="conf-vol"),
                        ],
                    )
                ],
                volumes=[
                    Volume(
                        name="scripts-vol",
                        configMap=ConfigMapVolumeSource(
                            defaultMode=555, name="my-set-config"
                        ),
                    ),
                    Volume(name="conf-vol", emptyDir=EmptyDirVolumeSource()),
                ],
            ),
        ),
        replicas=3,
    ),
)

print(get_yaml(z))