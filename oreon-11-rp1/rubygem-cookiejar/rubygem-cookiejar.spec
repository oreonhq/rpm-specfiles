%global source0_hash 4aa89d181e37f834d3c69efb4f774b58eb93fc87841cdc38a070d0a4e7aa1360

%global gem_name cookiejar	

Name: rubygem-%{gem_name}
Version: 0.3.3
Release: 20%{?dist}
Summary: Parsing and returning cookies in Ruby
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD	
URL: https://github.com/dwaite/cookiejar
Source0: https://rubygems.org/gems/cookiejar-%{version}.gem
# Remove rspec-collection_matchers dependency.
# https://github.com/dwaite/cookiejar/pull/36
Patch0: rubygem-cookiejar-0.3.3-Remove-rspec-collection_matchers-dependency.patch
# https://github.com/dorianmariefr/cookiejar2/pull/2
Patch1: cookiejar2-pr2-fix-regexp-3rd-arg.patch
# Ref: https://github.com/ruby/uri/issues/125
# Use URI::RFC2396_Parser explicitly for ruby34 (uri 1.0.1)
Patch2: cookiejar-uri-1_0-use-rfc2396_regexp-explicitly.patch
BuildRequires: rubygem(rspec)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildArch: noarch

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

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/contributors.json
%{gem_spec}
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/spec

%files doc
%{gem_docdir}  
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile

%changelog
%autochangelog
