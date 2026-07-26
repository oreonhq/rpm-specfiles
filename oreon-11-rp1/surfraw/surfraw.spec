%global source0_hash ad0420583c8cdd84a31437e59536f8070f15ba4585598d82638b950e5c5c3625

Name:           surfraw
Version:        2.3.0
Release:        17%{?dist}
Summary:        Shell Users Revolutionary Front Rage Against the Web
License:        LicenseRef-Fedora-Public-Domain
URL:            https://gitlab.com/surfraw/Surfraw
Source0:        http://surfraw.alioth.debian.org/dist/surfraw_%{version}.orig.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  %{_bindir}/pod2man
BuildRequires:  gawk

# Surfraw searches for a text-mode broser at configuration time, not
# at runtime. This is something probably to be changed upstream. We
# could depend on 'text-www-browser', but then we are not sure that
# this resolves to the same package at build and install time. So, for
# now, we simply pick one.
%global text_browser elinks
BuildRequires:  %{text_browser}
BuildRequires:  perl-generators
Requires:       %{text_browser}
Requires:       gawk

# For calling the graphical browser, we can rely on xdg-open.
Requires:       xdg-utils

%description
Surfraw provides a fast unix command line interface to a variety of
popular WWW search engines and other artifacts of power. It reclaims
google, altavista, babelfish, dejanews, freshmeat, research index,
slashdot and many others from the false-prophet, pox-infested heathen
lands of html-forms, placing these wonders where they belong, deep in
unix heartland, as god loving extensions to the shell.

Surfraw abstracts the browser away from input. Doing so lets it get on
with what it's good at. Browsing. Interpretation of linguistic forms
is handed back to the shell, which is what it, and human beings are
good at. Combined with netscape-remote or incremental text browsers,
such as links (http://artax.karlin.mff.cuni.cz/~mikulas/links/), w3m
(http://www.w3m.org/), and screen(1) a Surfraw liberateur is capable
of navigating speeds that leave GUI tainted idolaters agape with fear
and wonder.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --with-elvidir=%{_libexecdir}/surfraw \
           --with-graphical-browser=xdg-open \
           --with-text-browser=%{text_browser} \
           --disable-opensearch
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%dir %{_sysconfdir}/xdg/surfraw
%config(noreplace) %{_sysconfdir}/xdg/surfraw/*
%{_bindir}/sr
%{_bindir}/surfraw
%{_bindir}/surfraw-update-path
%{_libexecdir}/surfraw
%{_mandir}/man1/*.1*

%changelog
%autochangelog
