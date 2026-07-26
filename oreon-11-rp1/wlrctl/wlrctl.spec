%global source0_hash b5b3836091c41de09a832df1e5eb4747841d7ae670367e413487d5be7a5f2849

Name:           wlrctl
Version:        0.2.2
Release:        6%{?dist}
Summary:        Manipulate Wayland compositors using wlroots protocols

License:        MIT
URL:            https://git.sr.ht/~brocellous/wlrctl
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version} -p1

# Disable Werror
sed -e "/werror=true/d" -i meson.build

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/zsh/site-functions/_wlrctl
%{_mandir}/man1/wlrctl.1*

%changelog
%autochangelog
