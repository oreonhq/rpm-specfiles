%global source0_hash ed77bd6e0351bb00832dd4248cb4a6a69f5ccd08cf41f2f3806ae3732b7f0aa4

Name:           beansbinding
Version:        1.2.1
Release:        43%{?dist}
Summary:        Beans Binding (JSR 295) reference implementation

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://beansbinding.dev.java.net/
Source0:        https://beansbinding.dev.java.net/files/documents/6779/73673/beansbinding-1.2.1-src.zip
Patch0:         disable-doclint.patch
Patch1:         new-source-target.patch

BuildRequires:  ant-openjdk25 
BuildRequires:  ant-junit
BuildRequires:  java-25-devel

Requires:       java-25 >= 1:1.6.0
Requires:       javapackages-tools

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
In essence, Beans Binding (JSR 295) is about keeping two properties 
(typically of two objects) in sync. An additional emphasis is placed 
on the ability to bind to Swing components, and easy integration with 
IDEs such as NetBeans. This project provides the reference implementation.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
# remove all binary libs
find . -type f \( -iname "*.jar" -o -iname "*.zip" \) -print0 | xargs -t -0 %{__rm} -f

%build
%{ant} dist

%install
# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 dist/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}
%{__cp} -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc license.txt releaseNotes.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
%autochangelog
