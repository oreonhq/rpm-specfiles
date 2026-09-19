%global source0_hash 82c92d4df33a24a93d284cd6f0fa90313e34d07424c26fd6eae15aaea05fb1cb

%global pkg f

Name:           emacs-%{pkg}
Version:        0.21.0
Release:        4%{?dist}
Summary:        Modern API for working with files and directories in Emacs

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/rejeep/%{pkg}.el/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
BuildRequires:  emacs-dash
BuildRequires:  emacs-s
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-dash
Requires:       emacs-s
BuildArch:      noarch

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

%files
%doc CHANGELOG.org CONTRIBUTING.org README.org
%{_emacs_sitelispdir}/%{pkg}/

%changelog
%autochangelog
