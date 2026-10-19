%global source0_hash d21606fe7e197ee51eee1f8985d687297a3fb7cfa0505101e1ac9b321f4e7682
%global pkg rinari
%global pkgname Rinari
Name:             emacs-rinari
Version:          2.11  
Release:        1%{?dist}
Summary:        Ruby on rails minor mode for Emacs
License:          GPL-3.0-or-later
URL:              http://rinari.rubyforge.org/
Source0:        http://sagarun.fedorapeople.org/misc/rinari-20100815.tar.bz2
Source1:          emacs-rinari-init.el
BuildArch:        noarch
Requires:         emacs(bin) >= %{_emacs_version}
Obsoletes:        %{name}-el < 2.1-30.20100815git
Provides:         %{name}-el = %{version}-%{release}
# oreon:deps
BuildRequires:  emacs
BuildRequires:  texinfo
# /oreon:deps
%description
Rinari is a set of Emacs Lisp functions aimed towards 
making Emacs into a top-notch Ruby on rails development environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkg}

%build

/usr/bin/emacs -batch --no-init-file --no-site-file --eval '(progn (normal-top-level-add-subdirs-to-load-path))' -f batch-byte-compile *.el
%{_emacs_bytecompile} util/*el
%{_emacs_bytecompile} util/jump/*.el
makeinfo doc/rinari.texi
%install
rm -rf %{buildroot}
install -pm 755 -d  %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
install -pm 644 *.el* %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}/util/
install -pm 644 util/*.el* %{buildroot}%{_emacs_sitelispdir}/%{pkg}/util/
install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}/util/jump/
install -pm 644 util/jump/*.el* %{buildroot}%{_emacs_sitelispdir}/%{pkg}/util/jump/
install -pm 755 -d %{buildroot}%{_infodir}
install -pm 644 doc/%{pkg}.info %{buildroot}%{_infodir}/
install -pm 755 -d %{buildroot}%{_emacs_sitestartdir}/
install -pm 644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
