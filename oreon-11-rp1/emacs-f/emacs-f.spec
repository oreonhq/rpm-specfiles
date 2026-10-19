%global source0_hash 82c92d4df33a24a93d284cd6f0fa90313e34d07424c26fd6eae15aaea05fb1cb
%global pkg f
Name:           emacs-%{pkg}
Version:        0.21.0
Release:        1%{?dist}
Summary:        Modern API for working with files and directories in Emacs
License:        GPL-3.0-or-later
URL:            https://github.com/rejeep/%{pkg}.el/
Source0:        https://github.com/rejeep/%{pkg}.el//archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-dash
Requires:       emacs-s
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-dash
BuildRequires:  emacs-s
# /oreon:deps
%description
f.el is a modern API for working with files and directories in Emacs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}.el-%{version}

%build

%{_emacs_bytecompile} %{pkg}.el
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
