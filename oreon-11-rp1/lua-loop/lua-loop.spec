%global source0_hash 2c9000f5744ca84b6c0d58bd8fb1d8d71c2841b01a75b3b201a486f88ffda864

%define luaver 5.2
%define luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-loop
Version:        2.3
Release:        0.31.beta%{?dist}
Summary:        Class models for Lua

License:        MIT
URL:            http://loop.luaforge.net/
Source0:        http://luaforge.net/frs/download.php/3525/loop-2.3-beta.tar.gz

Requires:       lua >= %{luaver}

BuildArch:      noarch

%description
LOOP stands for Lua Object-Oriented Programming and is a set of
packages for supporting different models of object-oriented
programming in the Lua language.

LOOP models are mainly concerned with dynamicity, although there is an
attempt to keep them as simple and efficient as
possible. Additionally, LOOP uses fundamental Lua concepts like tables
(objects) and meta-tables (classes), traditionally used to enable an
object-oriented programming style, to provide a common ground for the
interoperability of objects and classes of its different models.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description    doc
LOOP stands for Lua Object-Oriented Programming and is a set of
packages for supporting different models of object-oriented
programming in the Lua language.

This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n loop-%{version}-beta
chmod +x lua/*.lua
for f in doc/*.css; do
  touch -r $f timestamp.txt
  sed -i 's|\r||' $f
  touch -r timestamp.txt $f
done

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{luapkgdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -pr lua/loop $RPM_BUILD_ROOT%{luapkgdir}
cp -p lua/*.lua $RPM_BUILD_ROOT%{_bindir}

%files
%doc LICENSE RELEASE
%{_bindir}/*.lua
%{luapkgdir}/*

%files doc
%doc doc/*

%changelog
%autochangelog
