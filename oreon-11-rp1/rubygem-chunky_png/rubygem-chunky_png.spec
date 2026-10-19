%global source0_hash 89d5b31b55c0cf4da3cf89a2b4ebc3178d8abe8cbaf116a1dba95668502fdcfe
%global gem_name chunky_png
Summary:        Pure ruby library for read/write, chunk-level access to PNG files
Name: rubygem-%{gem_name}
Version: 1.4.0
Release:        1%{?dist}
Patch0:  %{name}-pr169-object-regex_op-ruby32.patch
License: MIT
URL: https://chunkypng.com
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  ruby
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
This pure Ruby library can read and write PNG images without depending on
an external image library, like RMagick. It tries to be memory efficient and
reasonably fast.
It supports reading and writing all PNG variants that are defined in the
specification, with one limitation: only 8-bit color depth is supported. It
supports all transparency, interlacing and filtering options the PNG
specifications allows. It can also read and write textual metadata from PNG
files. Low-level read/write access to PNG chunks is also possible.
This library supports simple drawing on the image canvas and simple operations
like alpha composition and cropping. Finally, it can import from and export to
RMagick for interoperability.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
find %{buildroot} -iname .gitignore -exec rm -f {} \;
find %{buildroot} -iname .yardopts -exec rm -f {} \;
rm -f %{buildroot}%{gem_instdir}/.infinity_test
rm -rf %{buildroot}%{gem_instdir}/bin
%oreon_autofiles main

%check

pushd .%{gem_instdir}
sed -i "/require \"bundler\/setup\"/ s/^/#/" spec/spec_helper.rb
rspec spec
popd
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
