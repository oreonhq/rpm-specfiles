%global source0_hash 4aa89d181e37f834d3c69efb4f774b58eb93fc87841cdc38a070d0a4e7aa1360
%global gem_name cookiejar	
Name: rubygem-%{gem_name}
Version: 0.3.3
Release:        1%{?dist}
Summary:        Parsing and returning cookies in Ruby
License: LicenseRef-Callaway-BSD	
URL: https://github.com/dwaite/cookiejar
Source0:        https://rubygems.org/gems/cookiejar-%{version}.gem
Patch0: rubygem-cookiejar-0.3.3-Remove-rspec-collection_matchers-dependency.patch
Patch1: cookiejar2-pr2-fix-regexp-3rd-arg.patch
Patch2: cookiejar-uri-1_0-use-rfc2396_regexp-explicitly.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
The Ruby CookieJar is a library to help manage client-side cookies in pure
Ruby. It enables parsing and setting of cookie headers, alternating between
multiple 'jars' of cookies at one time (such as having a set of cookies for
each browser or thread), and supports persistence of the cookies in a JSON
string.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%check

pushd ./%{gem_instdir}
rspec -Ilib spec
popd	
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-cookiejar-doc -f %{oreon_filedir}/rubygem-cookiejar-doc.list

%changelog

%autochangelog
