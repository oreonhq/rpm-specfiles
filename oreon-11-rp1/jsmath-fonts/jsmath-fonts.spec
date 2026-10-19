%global source0_hash 2f4ef8e13aa21fc7fede1b0d47df5d3cc4cecbe5dc107c8afbfc4563a9e8055d
Summary:        A collection of Math symbol fonts
Name:	 jsmath-fonts 
Version: 20090708 
Release:        1%{?dist}
License: LicenseRef-Fedora-Public-Domain
Url: 	 http://www.math.union.edu/~dpvc/jsmath/welcome.html 
Source0:        http://www.math.union.edu/~dpvc/jsmath/download/TeX-fonts-linux.tgz
BuildArch: noarch
Requires: fontpackages-filesystem
# oreon:deps
BuildRequires:  fontpackages-devel
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n TeX-fonts-linux 

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_fontdir}
install -p -m644 *.ttf %{buildroot}%{_fontdir}/
%_font_pkg *.ttf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
