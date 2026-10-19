%global source0_hash 5397b8e3f323f23a687fccfb53bffc3b53e86702e7214f0a2ed7796adbb8836b
%global pkg flycheck
Name:           emacs-%{pkg}
Version:        39.0
Release:        1%{?dist}
Summary:        On the fly syntax checking for GNU Emacs
License:        GPL-3.0-or-later
URL:            https://www.flycheck.org/
Source0:        https://github.com/%{pkg}/%{pkg}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-dash
Requires:       emacs-pkg-info
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-dash
BuildRequires:  emacs-pkg-info
# /oreon:deps
%description
Flycheck is a modern on-the-fly syntax checking extension for GNU Emacs,
intended as replacement for the older Flymake extension which is part of GNU
Emacs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

%build

for i in *.el; do
    %{_emacs_bytecompile} $i
done
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 *.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
