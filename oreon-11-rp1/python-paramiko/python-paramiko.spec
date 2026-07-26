%global source0_hash 364658d3cabb7bf5a9e4dbbf7fdb8f9ef646c6af06a15c5a2cf8305666d5635a

Name:          python-paramiko
Version:       3.5.1
Release:       7%{?dist}
Summary:       SSH2 protocol library for python

# No version specified
License:       LGPL-2.1-or-later
URL:           https://github.com/paramiko/paramiko
Source0:       %{url}/archive/%{version}/paramiko-%{version}.tar.gz

# Remove pytest-relaxed, which depends on pytest4
# Can be removed when https://github.com/paramiko/paramiko/pull/1665/ is released
Patch3:        0003-remove-pytest-relaxed-dep.patch

# icecream not packaged in Fedora, nor needed for regular builds
Patch4:        0004-remove-icecream-dep.patch

# Avoid use of lexicon via invoke since we're avoiding invoke as a dependency;
# instead, use lexicon directly
Patch5:        0005-remove-invoke-dep.patch

BuildArch:     noarch

%global paramiko_desc \
Paramiko (a combination of the Esperanto words for "paranoid" and "friend") is\
a module for python 2.3 or greater that implements the SSH2 protocol for secure\
(encrypted and authenticated) connections to remote machines. Unlike SSL (aka\
TLS), the SSH2 protocol does not require hierarchical certificates signed by a\
powerful central authority. You may know SSH2 as the protocol that replaced\
telnet and rsh for secure access to remote shells, but the protocol also\
includes the ability to open arbitrary channels to remote services across an\
encrypted tunnel (this is how sftp works, for example).

%description
%{paramiko_desc}

%package -n python%{python3_pkgversion}-paramiko
Summary:       SSH2 protocol library for python
BuildRequires: python%{python3_pkgversion}-devel >= 3.6
BuildRequires: %{py3_dist lexicon} >= 2.0.1
BuildRequires: %{py3_dist pyasn1} >= 0.1.7
BuildRequires: %{py3_dist pytest}
Recommends:    %{py3_dist pyasn1} >= 0.1.7

%description -n python%{python3_pkgversion}-paramiko
%{paramiko_desc}

Python 3 version.

%package doc
Summary:       Docs and demo for SSH2 protocol library for python
BuildRequires: /usr/bin/sphinx-build
Requires:      %{name} = %{version}-%{release}

%description doc
%{paramiko_desc}

This is the documentation and demos.

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n paramiko-%{version}

chmod -c a-x demos/*
sed -i -e '/^#!/,1d' demos/*

%build
%pyproject_wheel

%install
%pyproject_install

sphinx-build -b html sites/docs/ html/
rm html/.buildinfo
rm -r html/.doctrees

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version}

%files -n python%{python3_pkgversion}-paramiko
%license LICENSE
%doc README.rst
%{python3_sitelib}/paramiko/
%{python3_sitelib}/paramiko-%{version}.dist-info/

%files doc
%doc html/ demos/

%changelog
%autochangelog
