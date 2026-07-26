%global source0_hash 6d9f089c5caeb02b3b1edacafa264c9459123f537e8e69207861864ae6b4bbe5

Name:           TE2PE
Version:        0.1.1
Release:        %autorelease
Summary:        Primitive TE to PE32 converter 

License:        WTFPL
URL:            https://github.com/LongSoft/TE2PE
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
This program tries to convert Terse Executable image used to store PEI modules
in different UEFI-compatible firmwares into normal PE32(+) image

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
$CC $CFLAGS %{name}.c -o %{name} $LDFLAGS

%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}

%files
%doc README.md
%{_bindir}/TE2PE

%changelog
%autochangelog
