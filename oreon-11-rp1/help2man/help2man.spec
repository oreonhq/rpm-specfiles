%global source0_hash none

# Supported build option:
#
# --with nls ... build this package with --enable-nls 

Name:           help2man
Summary:        Create simple man pages from --help output
Version:        1.49.3
Release:        9%{?dist}
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/help2man/
Source:         https://ftp.gnu.org/gnu/help2man/help2man-%{version}.tar.xz

%bcond_with nls

%{!?with_nls:BuildArch: noarch}

BuildRequires:  gcc
BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(strict)
%{?with_nls:BuildRequires: perl(Locale::gettext) /usr/bin/msgfmt}
%{?with_nls:BuildRequires: perl(Encode)}
%{?with_nls:BuildRequires: perl(I18N::Langinfo)}

%description
help2man is a script to create simple man pages from the --help and
--version output of programs.

Since most GNU documentation is now in info format, this provides a
way to generate a placeholder man page pointing to that resource while
still providing some useful information.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n help2man-%{version}

%build
%configure --%{!?with_nls:disable}%{?with_nls:enable}-nls --libdir=%{_libdir}/help2man
%{make_build}

%install
%{__make} install_l10n DESTDIR=$RPM_BUILD_ROOT
%{make_install}
%find_lang %name --with-man

%files -f %name.lang
%doc README NEWS THANKS
%license COPYING
%{_bindir}/help2man
%{_infodir}/*
%{_mandir}/man1/*

%if %{with nls}
%{_libdir}/help2man
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.49.3-9
- Prepare for Oreon 11 (RP1)
