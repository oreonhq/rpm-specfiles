%global source0_hash f63bc7349dcc1e2c7ee004dc80c5deb6732741c7f12e5015531ea55703b81028

Name:		ruby-bsearch
Version:	1.5
Release:	35%{?dist}
Summary:	Binary search library for Ruby

# SPDX confirmed
License:	Ruby OR GPL-2.0-only
URL:		http://0xcc.net/ruby-bsearch/
Source0:	http://0xcc.net/ruby-bsearch/%{name}-%{version}.tar.gz

# make it sure that the ruby used for build has
# the same abi as which is used at runtime
BuildRequires:	ruby(release)
Requires:	ruby(release)
BuildRequires:	ruby
BuildRequires:	ruby-devel
Provides:	ruby(bsearch) = %{version}-%{release}
BuildArch:	noarch

%description
Ruby/Bsearch is a binary search library for Ruby. It can search the FIRST or
LAST occurrence in an array with a condition given by a block.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{ruby_vendorlibdir}
%{__install} -c -p -m 644 bsearch.rb $RPM_BUILD_ROOT%{ruby_vendorlibdir}/

%check
cd tests ; sh test.sh
cd ..

%files
%doc ChangeLog bsearch.en.rd
%doc bsearch.png
%lang(ja) %doc bsearch.ja.rd
%{ruby_vendorlibdir}/bsearch.rb

%changelog
%autochangelog
