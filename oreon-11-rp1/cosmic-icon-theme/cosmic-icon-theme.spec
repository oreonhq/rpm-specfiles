%global source0_hash 1b15f26b5a6b876aaeb82fd51c1bf242b2c26bb5899105dd03168feba4896ae5
%global commit 5252095787cc96e2aed64604158f94e450703455
%global commitdatestring 2026-03-03 23:30:08 +0100
%global cosmic_minver 1.8.0
Name:           cosmic-icon-theme
Version: 1.9.0
Release:        1%{?dist}
Summary:        Icon theme for the COSMIC Desktop Environment
License:        CC-BY-SA-4.0
URL:            https://github.com/pop-os/cosmic-icons
Source0:        https://github.com/pop-os/cosmic-icons/archive/epoch-%{version}/cosmic-icons-%{version}.tar.gz
BuildArch:      noarch
Requires:       pop-icon-theme
Obsoletes: cosmic-icons < 0.1.0~git20240526.04.9aad1ab-2
Provides:  cosmic-icons = %{version}-%{release}
# oreon:deps
BuildRequires:  just
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cosmic-icons-epoch-%{version}
%oreon_prep
%build

%install
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
just rootdir=%{buildroot} prefix=%{_prefix} install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
