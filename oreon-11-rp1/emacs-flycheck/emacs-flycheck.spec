%global source0_hash 16392df534f310b5ab55e021bb68e5aecc71bc2638b6fa47cdf97f36b549c40f

%global pkg flycheck

Name:           emacs-%{pkg}
Version:        36.0
Release:        1%{?dist}
Summary:        On the fly syntax checking for GNU Emacs

License:        GPL-3.0-or-later
URL:            https://www.flycheck.org/
Source0:        https://github.com/%{pkg}/%{pkg}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-dash
BuildRequires:  emacs-pkg-info
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-dash
Requires:       emacs-pkg-info
BuildArch:      noarch

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

%files
%doc CHANGES.old CHANGES.rst MAINTAINERS README.md
%license COPYING
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el

%changelog
%autochangelog
