%global source0_hash 15f31bbd855131943397dded3a26003f2f5056e4c6a1a93d35ff7697b3f1e439

Name:           wlopm
Version:        1.0.0
Release:        %autorelease
Summary:        wlr-output-power-management-v1 client

License:        GPL-3.0-only
URL:            https://sr.ht/~leon_plickat/wlopm/
Source0:        https://git.sr.ht/~leon_plickat/wlopm/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(wayland-client) >= 1.20.0
BuildRequires:  pkgconfig(wayland-scanner)

%description
Wayland output power management.
Simple client implementing zwlr-output-power-management-v1.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

%build
%set_build_flags
%make_build

%install
install -d %{buildroot}%{bash_completions_dir}
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{bash_completions_dir}/%{name}

%changelog
%autochangelog
