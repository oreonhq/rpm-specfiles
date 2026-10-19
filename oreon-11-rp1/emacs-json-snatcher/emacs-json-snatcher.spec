%global source0_hash cb31a87db5efe5f2c04adaaa8260d9d9d9cc00b5e7289c17053fb6eba2e6d1d9
%global pkg json-snatcher
Name:           emacs-%{pkg}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Get the path to a JSON element in Emacs
License:        GPL-3.0-or-later
URL:            https://github.com/Sterlingg/%{pkg}
Source0:        https://github.com/Sterlingg/%{pkg}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
# /oreon:deps
%description
Say you're looking through a large JSON file, and see a value that you want to
extract programmatically. This Emacs extension will allow you to snatch the path
to this value.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

%build

%{_emacs_bytecompile} %{pkg}.el
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
