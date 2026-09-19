%global source0_hash ffb0dad67300c0e26d48397c1f4cf5c8413bff2f3b2d4f3e9e8653e6ef2e67cc

%global modname rpyc

Name:           python-%{modname}
Version:        6.0.2
Release:        %autorelease
Summary:        Transparent, Symmetrical Python Library for Distributed-Computing

License:        MIT
URL:            http://rpyc.wikidot.com/
Source0:        https://github.com/tomerfiliba/rpyc/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
RPyC, or Remote Python Call, is a transparent and symmetrical python library\
for remote procedure calls, clustering and distributed-computing.\
RPyC makes use of object-proxies, a technique that employs python's dynamic\
nature, to overcome the physical boundaries between processes and computers,\
so that remote objects can be manipulated as if they were local.}

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -S patch -p1
sed -i -e '/^#!\//, 1d' rpyc/cli/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}
# The binaries should not have .py extension
mv %{buildroot}%{_bindir}/rpyc_classic.py %{buildroot}%{_bindir}/rpyc_classic
mv %{buildroot}%{_bindir}/rpyc_registry.py %{buildroot}%{_bindir}/rpyc_registry

%files -n python3-%{modname} -f %{pyproject_files}
%{_bindir}/rpyc_*

%changelog
%autochangelog
