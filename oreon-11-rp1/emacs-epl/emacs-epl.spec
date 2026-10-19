%global source0_hash 8c0bba890f0e97c84f4dc8fb338eea9ac34dffdc1731042a2d85411b44461f66
%global pkg epl
Name:           emacs-%{pkg}
Version:        0.9
Release:        1%{?dist}
Summary:        Emacs Package Library
License:        GPL-3.0-or-later
URL:            https://github.com/cask/%{pkg}/
Source0:        https://github.com/cask/%{pkg}//archive/%{version}/%{name}-%{version}.tar.gz
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

%build

%{_emacs_bytecompile} %{pkg}.el
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
