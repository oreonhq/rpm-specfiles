%global source0_hash 1a3b5df5589b633de807f79cc8c2048bfadebf00b21fada0050483682d324519

Name:		pepc
Version:	1.6.10
Release:	%autorelease
Summary:	Power, Energy, and Performance Configurator

License:	BSD-3-Clause
Url:		https://github.com/intel/pepc
Source0:	%url/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:		pyproject.patch

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-tkinter
Requires:	python3-pepc = %{version}-%{release}

%description
Pepc stands for "Power, Energy, and Performance Configurator".
This is a command-line tool for configuring various Linux and Hardware 
power management features.

%package -n python3-%{name}
Summary:	Pepc Python libraries

%description -n python3-%{name}
Pepc Python libraries

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pepclibs pepctools pepcdata

%check
# skip heavy tests for non-x86_64 archs
%pytest \
%ifnarch x86_64 %{ix86}
  -k 'test_cpuinfo_get' \
%endif
  -v

%files
%license LICENSE.md
%doc README.md CHANGELOG.md
%{_bindir}/pepc

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
