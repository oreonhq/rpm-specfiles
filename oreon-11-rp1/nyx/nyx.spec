%global source0_hash 88521488d1c9052e457b9e66498a4acfaaa3adf3adc5a199892632f129a5390b
Summary:        Command-line monitor for Tor
License: GPL-3.0-only
URL: https://nyx.torproject.org
Source0:        https://files.pythonhosted.org/packages/source/n/nyx/nyx-%{version}.tar.gz
Patch0: nyx-2.1.0-replace-inspect.getargspec-usage.patch
BuildArch: noarch
Suggests: %{name}-doc = %{version}-%{release}
Provides: tor-arm = %{version}-%{release}
Obsoletes: tor-arm <= 1.4.5.0-17
Obsoletes: tor-arm-gui <= 1.4.5.0-17
Obsoletes: tor-arm-devel <= 1.4.5.0-17
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-nyx = %{version}-%{release}
# /oreon:deps
%description

%package doc
Summary: %summary
%description doc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -D -m 0644 nyx.1 %{buildroot}%{_mandir}/man1/nyx.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%{py3_test_envvars} %{python3} run_tests.py
%files
%files -n nyx-doc -f %{oreon_filedir}/nyx-doc.list

%changelog

%autochangelog
