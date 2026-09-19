%global source0_hash ac5619aa8cb46b7ccf1eae4e4bf26e1ab22123a895e8050a794406e127c9724c

%global	gem_name	minitest-around

Name:		rubygem-%{gem_name}
Version:	0.6.0
Release:	2%{?dist}

Summary:	Around block for minitest
License:	MIT
URL:		https://github.com/splattael/minitest-around

Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-test-missing-files.tar.gz
# Source1 is created from $ bash %%SOURCE2 %%version
Source2:	%{gem_name}-create-missing-test-files.sh

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(cucumber)
BuildArch:	noarch

%description
Alternative for setup/teardown dance.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version} -b 1

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

rm -f %{buildroot}%{gem_cache}

# Run the test suite
%check
cp -a \
	test/ \
	features/ \
	.%{gem_instdir}

export CUCUMBER_PUBLISH_QUIET=true

pushd .%{gem_instdir}
sed -i "/require 'bundler/ s/^/#/" test/test_helper.rb
env RUBYOPT=-Ilib \
	ruby -e 'Dir.glob "./test/*_{test,spec}.rb", &method(:require)'
env RUBYOPT=-Ilib \
	cucumber --tag 'not @todo' --tag 'not @rspec'
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
