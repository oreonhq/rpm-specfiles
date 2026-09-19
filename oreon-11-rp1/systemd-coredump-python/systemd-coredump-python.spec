%global source0_hash e419af86d1abd7e3f3a80b3bd5c65144ac00994d0dab737d8859538464f5a36d

Name:           systemd-coredump-python
Version:        3
Release:        %autorelease
Summary:        systemd-coredump helper to log Python exceptions

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/systemd/systemd-coredump-python
Source0:        https://github.com/systemd/systemd-coredump-python/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

BuildArch:      noarch

%global _description %{expand:
Python module which hooks into sys.excepthook to log backtraces in the journal.}

%description %_description

%package -n python3-systemd-coredump
Summary:        %{summary}
Conflicts:      systemd < 233

%description -n python3-systemd-coredump %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%py3_build

%install
%py3_install

# %%check
# there are no useful checks, the stuff in tests/ is only useful for development so far

%files -n python3-systemd-coredump
%license COPYING
%doc README
%{python3_sitelib}/systemd_coredump_exception_handler.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/systemd_coredump.pth
%{python3_sitelib}/systemd_coredump_python-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
