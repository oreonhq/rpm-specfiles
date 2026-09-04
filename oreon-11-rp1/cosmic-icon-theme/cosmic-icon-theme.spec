%global source0_hash d2d104f938aa544b5e1f286e93eb44908d06f9cf57799e48b36ad09d85fec268

# Generated using the scripts at # Generated using the scripts at https://forge.fedoraproject.org/cosmic/cosmic-packaging/src/branch/main/scripts

# While our version corresponds to an upstream tag, we still need to define
# these macros in order to set the VERGEN_GIT_SHA and VERGEN_GIT_COMMIT_DATE
# environment variables in multiple sections of the spec file.
%global commit 5252095787cc96e2aed64604158f94e450703455
%global commitdatestring 2026-03-03 23:30:08 +0100
%global cosmic_minver 1.0.9

Name:           cosmic-icon-theme
Version: 1.7.0
Release:        %autorelease
Summary:        Icon theme for the COSMIC Desktop Environment

License:        CC-BY-SA-4.0

URL:            https://github.com/pop-os/cosmic-icons

Source0:        https://github.com/pop-os/cosmic-icons/archive/epoch-%{version}/cosmic-icons-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  just

Requires:       pop-icon-theme

Obsoletes: cosmic-icons < 0.1.0~git20240526.04.9aad1ab-2
Provides:  cosmic-icons = %{version}-%{release}

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cosmic-icons-epoch-%{version}

%build

%install
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%dir %{_datadir}/icons/Cosmic
%{_datadir}/icons/Cosmic/*

%changelog
%autochangelog
