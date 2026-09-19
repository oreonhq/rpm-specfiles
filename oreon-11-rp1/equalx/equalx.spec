%global source0_hash 7f62e580206bc0e8e83a39bf4161bf6a6b0cd268507d5e1ad0781eeba1191f8b

Name:           equalx
Version:        0.7.1
Release:        30%{?dist}
Summary:        A graphical editor for writing LaTeX equations

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://equalx.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires:  desktop-file-utils
BuildRequires:  exempi-devel
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel 
BuildRequires: make
Requires:       ghostscript
Requires:       poppler-utils
Requires:       tex(latex)

%description
EqualX is an application that helps you to write equations in LaTeX
and to preview them in real-time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# fix line endings
sed 's|\r||g' LICENSE >LICENSE.new
touch -r LICENSE LICENSE.new
mv LICENSE.new LICENSE

%build
%{qmake_qt4}
make %{?_smp_mflags}

%install
install -D -p %{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -D -p -m 644 resources/icons/%{name}/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

%files
%doc LICENSE THANKS changelog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg

%changelog
%autochangelog
