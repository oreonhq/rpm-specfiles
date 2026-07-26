%global source0_hash 41ea26b13ad31938c6fdff98bfa8830cac286f2e73cef7920f9897616e6483c4

%global include_holidayparser  0
%{?_with_holidayparser: %{expand: %%global include_holidayparser 1}}

Name:           dayplanner
Version:        0.11
Release:        29%{?dist}
Summary:        An easy and clean Day Planner
Summary(pl):    Prosty i elegancki organizer
Summary(de):    Ein einfacher und klarer Tagesplaner
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.day-planner.org
Source0:        https://github.com/downloads/zerodogg/%{name}/%{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  gettext desktop-file-utils perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Locale::gettext)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
%if 0%{?fedora} && 0%{?fedora} >= 19
BuildRequires:  perl(autodie)
BuildRequires:  perl-generators
%endif
BuildRequires: make
Requires:       hicolor-icon-theme
Requires:       perl(Locale::gettext)

%description
Day Planner is a simple time management program.

Day Planner is designed to help you easily manage your time.
It can manage appointments, birthdays and more. It makes sure you
remember your appointments by popping up a dialog box reminding you about it.

%description -l pl
Day Planner is a prosty program do zarządzania czasem.

Day Planner jest zaprojektowany aby pomóc Tobie łatwo zarządzać Twoim czasem.
Może zarządzać spotkaniami, urodzinami i innymi. Możesz być pewnym że będziesz
pamiętał o spotkaniach przez wyskakujące okna dialogowe przypominające o nich.

%description -l de
Day Planner ist ein einfaches Zeitverwaltungsprogram.

Day Planner hilft Ihnen, Ihre Termine einfach zu verwalten. Es kann Termine, 
Geburtstage und vieles mehr speichern. Um sicherzustellen, dass Sie keine 
Termine verpassen, erinnert Sie Day Planner mit einem Dialogfenster daran.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# filter out all unwanted perl related Requires and Provides
cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
sed -e '/perl(DP::.*)/d' |\
sed -e '/perl(Date::HolidayParser)/d'
EOF

%global __perl_provides %{_builddir}/%{name}-%{version}/%{name}-prov
chmod +x %{__perl_provides}

cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(DP::.*)/d' |\
sed -e '/perl(Date::HolidayParser)/d'
EOF

%global __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req
chmod +x %{__perl_requires}	

%build
# nothing to build

%install
%if 0%{?include_holidayparser}
make install DESTDIR=%{buildroot} prefix=%{_prefix}
%else
make install DESTDIR=%{buildroot} prefix=%{_prefix}
%endif

# Install hicolor icons
for size in 16 24 32 48; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
  install -pm644 art/%{name}-${size}x${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

rm -f %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -f %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Install desktop file
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor="fedora"                    \
%endif
  --remove-category=X-MandrivaLinux-Office-TimeManagement \
  --dir=%{buildroot}%{_datadir}/applications           \
  ./doc/%{name}.desktop

# Chmod
find %{buildroot}%{_datadir}/%{name} -name \*.pm -exec chmod 0644 {} \;

# Find the localization
%find_lang %{name}

%files -f dayplanner.lang
%doc AUTHORS COPYING NEWS THANKS TODO 
%doc ./doc/{*_Spec,EnvironmentVariables,HACKING,README.*,TESTCASES,TODO_DPS}
%{_bindir}/%{name}*
%{_datadir}/%{name}
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_mandir}/man1/dayplanner*.1*

%changelog
%autochangelog
