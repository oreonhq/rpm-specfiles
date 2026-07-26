%global source0_hash a0597b0ed8913a834968616db850c15b636244b0c599e87f6f9c65844bc05546

%global pkg ansible

Name:           emacs-%{pkg}
Version:        0.4.2
Release:        3%{?dist}
Summary:        Ansible minor mode

License:        GPL-2.0-or-later
URL:            https://gitlab.com/%{name}/%{name}
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-f
BuildRequires:  emacs-s
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-f
Requires:       emacs-s
BuildArch:      noarch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{_emacs_bytecompile} %{pkg}.el

%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
cp -a dict/ snippets/ $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el

%changelog
%autochangelog
