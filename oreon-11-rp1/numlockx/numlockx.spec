%global source0_hash e468eb9121c94c9089dc6a287eeb347e900ce04a14be37da29d7696cbce772e4

Name:           numlockx
Version:        1.2
Release:        30%{?dist}
Summary:        Turns on NumLock after starting X

License:        MIT
URL:            http://ktown.kde.org/~seli/numlockx/
Source0:        http://ktown.kde.org/~seli/numlockx/numlockx-%{version}.tar.gz
Source1:        numlockx.sh

BuildRequires:  gcc make
BuildRequires:  libX11-devel libXtst-devel libXext-devel libXt-devel
Requires:       xorg-x11-xinit

%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%make_build

%install
%make_install
install -p -D %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/numlockx.sh

%files
%license LICENSE
%doc AUTHORS README
%{_bindir}/numlockx
%{_sysconfdir}/X11/xinit/xinitrc.d/numlockx.sh

%changelog
%autochangelog
