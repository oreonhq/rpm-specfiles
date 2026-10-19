%global source0_hash 22431e3d426191ccca408cea6ef4f2832a83dc0cd0ce63d2930f52178be5bc90
Name:       loook
Version:    0.9.1
Release:        1%{?dist}
Summary:        OpenOffice.org document search tool
License:    GPL-2.0-or-later
URL:        http://mechtilde.de/Loook/
Source0:        http://mechtilde.de/Loook/Downloads/%{name}-%{version}.tar.gz
BuildArch:  noarch
Requires:   python3-tkinter
Requires:   hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
# /oreon:deps
%description
Loook is a simple Python tool that searches for text strings in OpenOffice.org
(and StarOffice 6.0 or later) files. It works under Linux, Windows and
Macintosh. AND, OR and phrase searches are supported. It doesn't create an
index, but searching should be fast enough unless you have really many files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
install -Dpm 0755 %{name}.py $RPM_BUILD_ROOT%{python3_sitelib}/%{name}/%{name}.py
mkdir -p $RPM_BUILD_ROOT%{_bindir}
ln -s %{python3_sitelib}/%{name}/%{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dpm 0644 %{name}.png $RPM_BUILD_ROOT%{_datadir}/hicolor/icons/24x24/%{name}.png
install -Dpm 0644 man/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
