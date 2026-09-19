%global source0_hash fba2451fc8cd4494fc0025264b67be49a58e020e01c65e5d5d2c43f84f53ce84

Name:           R-keyring
Version:        %R_rpm_version 1.4.1
Release:        %autorelease
Summary:        Access the System Credential Store from R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libsecret-1)

%description
Platform independent API to access the operating system's credential store.
Currently supports: Keychain on macOS, Credential Store on Windows, the Secret
Service API on Linux, and a simple, platform independent store implemented with
environment variables. Additional storage back-ends can be added easily.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
