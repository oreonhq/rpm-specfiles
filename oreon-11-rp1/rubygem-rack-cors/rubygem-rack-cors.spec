%global source0_hash 4702644ac6d63ebbddff372a3cd4cd573513287e3524b5a5415f678970057a4b

%global gem_name rack-cors

Name:           rubygem-%{gem_name}
Version:        1.1.1
Release:        15%{?dist}
Summary:        Middleware for enabling Cross-Origin Resource Sharing in Rack apps

License:        MIT
URL:            https://github.com/cyu/rack-cors
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/cyu/rack-cors/pull/266
Patch0:         rack-cors-pr266-minitest-mocha-compatibility.patch
# Fix compatibility with Rack3, taken from following changes:
#   Add missing include for Rack3
#     https://github.com/cyu/rack-cors/pull/262
#   Rack3: Rack::Lint does not accept uppercase character in header name
#     commit: a48a55807afa49f2906de69e101d2c196a65ffed
#     commit: 75d4510378462b098e092a0461cf3a1788bf9a6a
#     commit: 41511184d1158c855226811028eb102ed88b82ca
Patch1:         rack-cors-1.1.1-rack3-compat.patch

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(logger)
BuildRequires:  rubygem(minitest) >= 5.11.0
BuildRequires:  rubygem(mocha) >= 1.6.0
BuildRequires:  rubygem(rack-test)

%description
Middleware that will make Rack-based apps CORS compatible.

Fork the project here: https://github.com/cyu/rack-cors.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# ref: https://github.com/cyu/rack-cors/pull/286
%gemspec_add_dep -g logger -s %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ruby -rminitest/autorun -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%license %{gem_instdir}/LICENSE.txt
%dir %{gem_instdir}/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/test/
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
