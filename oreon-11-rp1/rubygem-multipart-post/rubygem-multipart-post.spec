%global source0_hash 5eed114b767a1f4328c7d91404b4a012845ca680791e04ff72a73d2a28dad3ec

# Generated from multipart-post-1.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name multipart-post

Name: rubygem-%{gem_name}
Version: 2.2.3
Release: 8%{?dist}
Summary: A multipart form post accessory for Net::HTTP
License: MIT
URL: https://github.com/socketry/multipart-post
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/socketry/multipart-post.git && cd multipart-post
# git archive -v -o multipart-post-2.2.3-spec.tar.gz v2.2.3 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Adds a streamy multipart form post capability to Net::HTTP. Also supports other
methods besides POST.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

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

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec

# Avoid Bundler.
sed -i '/bundler\/setup/ s/^/#/' spec/spec_helper.rb

rspec -rspec_helper spec
popd

%files
# TODO: LICENSE file request:
# https://github.com/socketry/multipart-post/issues/97
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
