%global source0_hash 88d04f1910190db5753b0efce878c56a5e47fbadd5fef49e13abda2880b95f69

%global gittag 1.0.3
%global debug_package %{nil}

Name: pwkickstart
Version: %{gittag}
Release: 20%{?dist}
Summary: Helps to generate kickstart passwords
License: MIT
URL: https://github.com/lzap/pwkickstart
Source0: https://github.com/lzap/%{name}/archive/%{gittag}.tar.gz

Requires:	python3
Requires:	python3-crypt-r

BuildRequires:	txt2man

%description
Helps to generate kickstart passwords, similarly to grub-crypt tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{gittag}

%build
txt2man -t %{name} -r %{version} -s 1 README > %{name}.1

%install
install -m 755 -D %{name} %{buildroot}/%{_bindir}/%{name}
install -m 644 -D %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE

%changelog
%autochangelog
