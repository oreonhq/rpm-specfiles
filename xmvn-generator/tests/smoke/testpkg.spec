%global __xmvngen_debug 1
%global __xmvngen_provides_generators org.fedoraproject.xmvn.generator.jpms.JPMSGeneratorFactory
%global __xmvngen_requires_generators %{nil}
%global __xmvngen_post_install_hooks org.fedoraproject.xmvn.generator.transformer.TransformerHookFactory

Name:       testpkg
Epoch:      42
Version:    1.2.3
Release:    1.fc22
Summary:    test package
License:    DUMMY
URL:        file:/dev/null
BuildArch:  noarch

%description
test package

%install
touch file.txt
echo Automatic-Module-Name: foo.module >mf
echo Rpm-Version: 4.5.6 >>mf
jar cfm out.jar mf file.txt
install -D out.jar %{buildroot}%{_javadir}/sub/some.jar
echo INSTALL DONE

%files
%{_javadir}

%changelog
