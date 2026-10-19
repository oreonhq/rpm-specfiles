%global source0_hash e224490fd2841798a93442cb51f8dda42959ac0d05713421b717243ccf910104
Name:		ruby-romkan
Version:	0.4
Release:        36%{?dist}
Summary:        Romaji <-> Kana conversion library for Ruby
License:	Ruby OR GPL-2.0-only
URL:		http://0xcc.net/ruby-romkan/
Source0:        http://0xcc.net/ruby-romkan/%{name}-%{version}.tar.gz
Requires:	ruby(abi) = %{rubyabi}
Provides:	ruby(romkan) = %{version}-%{release}
BuildArch:	noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(abi)
BuildRequires:  ruby-devel
# /oreon:deps
%description
Ruby/Romkan is a Romaji <-> Kana conversion library for Ruby. It can
convert a Japanese Romaji string to a Japanese Kana string or vice
versa.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i '1 i\
# -*- encoding:euc-jp -*-' romkan.rb

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{ruby_vendorlibdir}
%{__install} -c -p -m 644 romkan.rb $RPM_BUILD_ROOT%{ruby_vendorlibdir}/
%oreon_autofiles main

%check

sh test.sh
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
