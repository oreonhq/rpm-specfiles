%global source0_hash c29ada31c0f750b1d10c1a20442d015dc5052b80548b68d421bfded7adde2f87

%global gem_name dalli

# Depends on Rails and its needed by Rails
%bcond_with tests

Name: rubygem-%{gem_name}
Version: 3.2.0
Release: 11%{?dist}
Summary: High performance memcached client for Ruby
License: MIT
URL: https://github.com/petergoldstein/dalli
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests are not shipped with the gem, you may get them like so
# git clone https://github.com/petergoldstein/dalli.git --no-checkout
# git -C dalli archive -v -o dalli-3.2.0-tests.txz v3.2.0 test/
Source1: %{gem_name}-%{version}-tests.txz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if %{with tests}
BuildRequires: memcached
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(connection_pool)
%endif
BuildRequires: ruby
Requires:  rubygem(base64)
BuildArch: noarch

%description
High performance memcached client for Ruby

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
%if %{with tests}
pushd .%{gem_instdir}
# Symlink tests into place
ln -s %{_builddir}/test .

sed -i '/bundler/ s/^/#/' test/helper.rb
ruby -Ilib:test -rdalli -e "Dir.glob('./test/test_*.rb').sort.each{ |x| require x }"
popd
%endif

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/History.md
%{gem_instdir}/Gemfile

%changelog
%autochangelog
