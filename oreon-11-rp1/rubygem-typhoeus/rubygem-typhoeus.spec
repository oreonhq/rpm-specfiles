%global source0_hash bacc41c23e379547e29801dc235cd1699b70b955a1ba3d32b2b877aa844c331d

%global gem_name typhoeus

Name: rubygem-%{gem_name}
Version: 1.6.0
Release: 1%{?dist}
Summary: Parallel HTTP library on top of libcurl multi
License: MIT
URL: https://github.com/typhoeus/typhoeus
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix Ruby 3.0 compatibility.
# https://github.com/typhoeus/typhoeus/pull/668
Patch0: typhoeus-1.4.0-Fix-Ruby-3-0-compatibility.patch
# Fix testsuite assertion with curl 8.9
# https://github.com/typhoeus/typhoeus/pull/724/
Patch1: typhoeus-1.4.0-support-curl-8_9-msg.patch
# Fix Rack 3 compatibility
# https://github.com/typhoeus/typhoeus/pull/731
Patch2: rubygem-typhoeus-1.4.1-Fix-Rack-3-compatibility.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(dalli)
BuildRequires: rubygem(ethon) >= 0.7.0
BuildRequires: rubygem(faraday)
BuildRequires: rubygem(redis)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(sinatra)
BuildRequires: rubygem(webrick)
# For Rack 3+ compatibility, where Rackup is split into separate rubygem-rackup
# package.
BuildRequires: %{_bindir}/rackup
BuildArch: noarch

%description
Like a modern code version of the mythical beast with 100 serpent heads,
Typhoeus runs HTTP requests in parallel while cleanly encapsulating handling
logic.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Drop shebang.
sed -i -e '/^#!/d' %{buildroot}%{gem_instdir}/spec/support/server.rb

%check
pushd .%{gem_instdir}
# Don't use Bundler.
sed -i -e '/[bB]undler/ s/^/#/' spec/spec_helper.rb

rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Guardfile
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/UPGRADE.md
%{gem_instdir}/perf
%{gem_instdir}/spec
%{gem_instdir}/typhoeus.gemspec

%changelog
%autochangelog
