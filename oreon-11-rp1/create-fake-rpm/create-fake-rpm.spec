%global source0_hash 351019796a6549c57fd993a90c083b7093a5f3f5b19965e53fbbb772c4bd99d8

Name:           create-fake-rpm
Version:        5
Release:        10%{?dist}
License:        GPL-2.0-or-later
Summary:        Generate fake (S)RPM
BuildArch:      noarch
# Sources can be obtained by
# git clone git://github.com/xsuchy/create-fake-rpm.git
# cd create-fake-rpm
# tito build --tgz
Source0:        %{name}-%{version}.tar.gz
URL:            https://github.com/xsuchy/create-fake-rpm

Requires:       rpm-build
BuildRequires:  asciidoc
BuildRequires:  libxslt

%description
A tool to generate an (s)rpm with faked provides.

It may be useful when you install some library/module/application manually -
without having an RPM package.

E.g., when you

    pip install somepackage

And when some RPM package `Requires: python-somepackage` then /usr/bin/rpm
refuses to install such package, because `python-somepackage` is not present
on your system.

RPMDB does not know what you know. So you can run:

    create-fake-rpm --build python-somepackage python3dist(somepackage)

This create package `fake-python-somepackage-0-0.noarch.rpm` which provides:
"python-somepackage" and "python3dist(somepackage)".
You can install it using:

    dnf install fake-python-somepackage-0-0.noarch.rpm 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
a2x -d manpage -f manpage create-fake-rpm.1.asciidoc
sed -i 's|^TEMPLATEDIR=.*|TEMPLATEDIR=%{_datadir}/%{name}/|' create-fake-rpm

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m755 -p create-fake-rpm %{buildroot}%{_bindir}
install -m644 -p create-fake-rpm.1 %{buildroot}/%{_mandir}/man1/
cp -a template/template.spec %{buildroot}%{_datadir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_bindir}/create-fake-rpm
%doc %{_mandir}/man1/create-fake-rpm.1*
%{_datadir}/%{name}

%changelog
%autochangelog
