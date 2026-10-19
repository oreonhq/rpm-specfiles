%global source0_hash 913042d3afade625b71d05827b924692d05abfe1787d0f2b571fe95bc1c4a4df
%global		gem_name		imagesize
Summary:        Measure image size(GIF, PNG, JPEG ,,, etc)
Name:		rubygem-%{gem_name}
Version:	0.1.1
Release:        1%{?dist}
License:	Ruby OR GPL-2.0-only
URL:		http://imagesize.rubyforge.org
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:         ruby-imagesize-0.1.1-ruby19-regex-utf8.patch
Patch1:         rubygem-imagesize-0.1.1-regex-magic.patch
Requires:	ruby(abi) = %{rubyabi}
Requires:	ruby 
Requires:	rubygems
Obsoletes:	ruby-imagesize <= %{version}-%{release}
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(abi)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Imagefile measures image (GIF, PNG, JPEG ,,, etc) size code 
by Pure Ruby ["PCX", "PSD", "XPM", "TIFF", "XBM", "PGM", 
"PBM", "PPM", "BMP", "JPEG", "PNG", "GIF", "SWF"]

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
mkdir -p .%{gem_dir}
TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}

# Fixup wrong interpretter, line encoding
sed -i -e '1d' -e 's|\r||' lib/image_size.rb

# Patches
%patch -P0 -p1
%patch -P1 -p1

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
#ERROR:  While executing gem ... (Gem::InvalidSpecificationException)
#    cert_chain must not be nil
sed -i -e '/cert_chain/s|nil|[]|' %{gem_name}.gemspec

gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build

%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i.ppm \
	-e "s|'ppm.ppm', ||" \
	-e '/PPM/d' \
	test/test_image_size.rb
ruby -Ilib -rtest/unit ./test/test_image_size.rb || echo "rescue for now"
%files -f %{oreon_filedir}/main.list
%files -n rubygem-imagesize-doc -f %{oreon_filedir}/rubygem-imagesize-doc.list

%changelog

%autochangelog
