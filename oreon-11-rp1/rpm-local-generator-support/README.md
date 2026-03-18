# rpm-local-generator-support

This package ships `%{_fileattrsdir}/local_generator.attr` file, which enables
`local_generator` for RPM. This is useful in cases, where package ships
generators and wants to use them internally. In such case, it is possible to
redefine the generator macros:

~~~
... snip ...

Source1: generator.req
BuildRequires: rpm-local-generator-support

%global __local_generator_requires bash %{SOURCE9}"

... snip ...
~~~

More details about the idea and purpose of this file can be find here:

https://github.com/rpm-software-management/rpm/issues/782#issuecomment-1747200612
https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/3MHROKOM53HM6NF7RGGLFBIQFG5IEIQG/

