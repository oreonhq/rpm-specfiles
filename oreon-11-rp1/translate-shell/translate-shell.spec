%global source0_hash f949f379779b9e746bccb20fcd180d041fb90da95816615575b49886032bcefa
%global debug_package %{nil}
Summary:        Command-line translator using Google Translate, Bing, Yandex etc
Name:           translate-shell
Version:        0.9.7.1
Release:        1%{?dist}
License:        Unlicense
URL:            https://www.soimort.org/translate-shell/
Source0:        https://github.com/soimort/translate-shell/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       gawk
Requires:       curl
Requires:       rlwrap
# oreon:deps
BuildRequires:  gawk
BuildRequires:  make
# /oreon:deps
%description
Translate Shell (formerly Google Translate CLI) is a command-line translator
powered by Google Translate, Bing Translator, Yandex.Translate, and
Apertium. It gives instant access to one of these translation engines from
the command-line.

Backs the translation engine used by plasma-applet-translator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

make PREFIX=%{_prefix} build
%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
