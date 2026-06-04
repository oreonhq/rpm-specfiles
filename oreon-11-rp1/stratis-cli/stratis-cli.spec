%global source0_hash 1c7255e871504d3df00ebb73ffbd78455b085b4707c84a3fbdabdfd9f9d1daa6

Name:           stratis-cli
Version:        3.8.3
Release:        %autorelease
Summary:        Command-line tool for interacting with the Stratis daemon

License:        Apache-2.0
URL:            https://github.com/stratis-storage/stratis-cli
Source0:        https://github.com/stratis-storage/stratis-cli/archive/refs/tags/v3.8.3/stratis-cli-3.8.3.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{_bindir}/a2x
%if 0%{?rhel}
BuildRequires:  python3-dateutil
BuildRequires:  python3-dbus-client-gen
BuildRequires:  python3-dbus-python-client-gen
BuildRequires:  python3-justbytes
BuildRequires:  python3-packaging
BuildRequires:  python3-psutil
BuildRequires:  python3-wcwidth
%endif

# Require the version of stratisd that supports a compatible D-Bus interface
Requires:       (stratisd >= 3.8.2 with stratisd < 4.0.0)

# Exclude the same arches for stratis-cli as are excluded for stratisd
ExclusiveArch:  %{rust_arches} noarch
%if 0%{?rhel}
ExcludeArch:    i686
%endif
BuildArch:      noarch

%description
stratis provides a command-line interface (CLI) for
interacting with the Stratis daemon, stratisd. stratis
interacts with stratisd via D-Bus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
a2x -f manpage docs/stratis.txt

%install
%pyproject_install
%pyproject_save_files -l stratis_cli
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man8 docs/stratis.8

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/stratis
%{_mandir}/man8/stratis.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.8.3-1
- Prepare for Oreon 11 (RP1)
