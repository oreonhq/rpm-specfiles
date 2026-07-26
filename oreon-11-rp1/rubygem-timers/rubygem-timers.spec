%global source0_hash f45ca1b8ce6b26e29226c2144c512801a9019c3e781054d878c205cb0fd8500d

# Generated from timers-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name timers

Name: rubygem-%{gem_name}
Version: 4.0.1
Release: 21%{?dist}
Summary: Pure Ruby one-shot and periodic timers
License: MIT
URL: https://github.com/celluloid/timers
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(hitimes)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Schedule procs to run after a certain time using any API that accepts a timeout

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

sed -i '/#!/d' %{buildroot}%{gem_instdir}/Rakefile

%check
pushd .%{gem_instdir}
# Bundler is used only for development. No need to install it.
sed -i '/bundler/ s/^/#/' spec/spec_helper.rb

# We don't care about code coverage.
sed -i '/[Cc]overalls/ s/^/#/' spec/spec_helper.rb

# ruby-prof is not in Fedora yet, but I don't think we are interested in
# profiler output anyway.
# https://bugzilla.redhat.com/show_bug.cgi?id=1116021
sed -i '/ruby-prof/ s/^/#/' spec/performance_spec.rb

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
%doc %{gem_instdir}/AUTHORS.md
%{gem_instdir}/CHANGES.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/timers.gemspec

%changelog
%autochangelog
