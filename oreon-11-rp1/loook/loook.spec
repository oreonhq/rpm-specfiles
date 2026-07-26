%global source0_hash 31153772d8860c3d30412ed205fd7601ad44a0f3618cb7822cafadc5c9a4be80

Name:       loook
Version:    0.9.0
Release:    7%{?dist}
Summary:    OpenOffice.org document search tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        http://mechtilde.de/Loook/
Source0:    http://mechtilde.de/Loook/Downloads/%{name}-%{version}.tar.gz

BuildArch:  noarch

Requires:   python3-tkinter
Requires:   hicolor-icon-theme

BuildRequires: python3-devel
BuildRequires: desktop-file-utils

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

%files
%{python3_sitelib}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/hicolor/icons/24x24/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
