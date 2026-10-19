%global source0_hash 6045283b98e004a683b13a636409ba691401d2ae9e5122d244c151972e923341
Name:           remind
Version:        06.03.03
Release:        1%{?dist}
Summary:        Sophisticated calendar and alarm program
License:        GPL-2.0-only AND BSD-2-Clause AND (GPL-2.0-only AND LicenseRef-Fedora-Public-Domain) AND LicenseRef-Fedora-Public-Domain
URL:            https://dianne.skoll.ca/projects/remind/
Source0:        https://dianne.skoll.ca/projects/%{name}//download/%{name}-%{version}.tar.gz
Patch:          use-system-libjsonparser.diff
Recommends:     remind-tools
Recommends:     remind-gui
Recommends:     remind-doc
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl(Cairo)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Pango)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(json-parser)
BuildRequires:  tzdata
# /oreon:deps
%description
Remind is a sophisticated calendar and alarm program. It includes the following
features:

 - A sophisticated scripting language and intelligent handling of exceptions
   and holidays
 - Plain-text, PDF, PostScript and HTML output
 - Timed reminders and pop-up alarms
 - A friendly graphical front-end for people who don't want to learn the
   scripting language
 - Facilities for both the Gregorian and Hebrew calendars
 - Support for 12 different languages

%package        doc
Summary:        Documentation for remind, a sophisticated calendar and alarm program
License:        GPL-2.0-only
BuildArch:      noarch
%description    doc
Documentation and information on how to use remind

%package        gui
Summary:        GUI for remind, a sophisticated calendar and alarm program
License:        GPL-2.0-only
BuildArch:      noarch
Provides:       tkremind = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       tcl
Requires:       tcllib
Requires:       tk >= 8.0
Suggests:       google-noto-fonts
%description    gui
Tkremind provides a GUI which allows viewing a calendar and adding or editing
reminders without learning the syntax of Remind.

%package        tools
Summary:        Additional tools for remind
License:        GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only
%description    tools
Tools to convert the remind output to ps, pdf or html as well as example files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{name}-%{version}
# Disable packlist and perllocal update
sed -i 's|\$(PERL) Makefile.PL|\$(PERL) Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"|g' rem2pdf/Makefile.top.in

# json-parser is in fedora; remove bundled copies
rm src/json.h
rm src/json.c

%build

%configure
%make_build
%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/tkremind.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n remind-doc -f %{oreon_filedir}/remind-doc.list
%files -n remind-gui -f %{oreon_filedir}/remind-gui.list
%files -n remind-tools -f %{oreon_filedir}/remind-tools.list

%changelog

%autochangelog
