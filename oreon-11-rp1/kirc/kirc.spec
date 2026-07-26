%global source0_hash a45172198873fb34c64150262be4515a7be268a5c00566c79f03a8ea2dd7900e

Name:           kirc
Version:        0.3.2
Release:        %autorelease
Summary:        Tiny IRC client written in POSIX C99

License:        MIT
URL:            https://github.com/mcpcpc/kirc
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
kirc ("KISS for IRC") is a tiny open-source Internet Relay Chat (IRC) client
designed with usability and cross-platform compatibility in mind.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%set_build_flags
%make_build

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README.md
%{_bindir}/kirc
%{_mandir}/man1/kirc.1*

%changelog
%autochangelog
