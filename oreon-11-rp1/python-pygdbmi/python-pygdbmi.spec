%global source0_hash 5c52a37211d55eeeaf5c06eacc8e8d49e9dacfd36a526d3534b4a5d5f5ee94d9

Name:           python-pygdbmi
Version:        0.11.0.0
Release:        %autorelease
Summary:        Get Structured Output from GDB's Machine Interface 
License:        MIT
URL:            https://github.com/cs01/pygdbmi
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pytest
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gdb

%global _description \
GDB/MI is a line based machine oriented \
text interface to GDB and is activated by \
specifying using the --interpreter command \
line option (see Mode Options). It is\
specifically intended to support the development\
of systems which use the debugger as just one\
small component of a larger system.

%description %{_description}

%package -n python3-pygdbmi
Summary:        %{summary}

%description -n python3-pygdbmi %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pygdbmi-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pygdbmi

%check
# tests/test_gdbcontroller.py fails: https://bugzilla.redhat.com/2291356
%pytest --ignore tests/test_gdbcontroller.py

%files -n python3-pygdbmi -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
