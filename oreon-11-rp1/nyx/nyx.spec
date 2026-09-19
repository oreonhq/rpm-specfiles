%global source0_hash 88521488d1c9052e457b9e66498a4acfaaa3adf3adc5a199892632f129a5390b

%global _description\
Nyx is a command-line monitor for Tor. With this you can get detailed\
real-time information about your relay such as bandwidth usage,\
connections, logs, and much more.

Name: nyx
Version: 2.1.0
Release: 29%{?dist}
Summary: Command-line monitor for Tor
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
URL: https://nyx.torproject.org
Source0: %{pypi_source}
# https://github.com/torproject/nyx/issues/49
Patch0: nyx-2.1.0-replace-inspect.getargspec-usage.patch
BuildArch: noarch
BuildRequires: python3-devel
Suggests: %{name}-doc = %{version}-%{release}
Provides: tor-arm = %{version}-%{release}
Obsoletes: tor-arm <= 1.4.5.0-17
Obsoletes: tor-arm-gui <= 1.4.5.0-17
Obsoletes: tor-arm-devel <= 1.4.5.0-17

%description %_description

%package doc
Summary: %summary

%description doc %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}
install -D -m 0644 nyx.1 %{buildroot}%{_mandir}/man1/nyx.1

%check
%pyproject_check_import
%{py3_test_envvars} %{python3} run_tests.py

%files -f %{pyproject_files}
%{_bindir}/%{name}

%files doc
%doc web
%{_mandir}/man1/nyx.1*

%changelog
%autochangelog
