# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 62fec2273016fb6e69b18635e696fd2c91953af9cbe757b341721aec2232432e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

BuildArch: noarch

%global archivename All_KhmerOS_%{version}

Version:        5.0
Release:        47%{?dist}
License:        LGPL-2.1-or-later
URL:            http://www.khmeros.info/en/fonts

%global common_description %{expand:
The Khmer OS fonts include Khmer and Latin alphabets, and they have equivalent
sizes for Khmer and English alphabets, so that when texts mix both it is not
necessary to have different point sizes for the text in each language.

They were created by Danh Hong of the Cambodian Open Institute.}

%global foundry           Khmer OS
%global fontlicenses      License.txt

%global fontfamily1       Battambang
%global fontsummary1      Battambang font
%global fontpkgheader1    %{expand:
Obsoletes: khmeros-battambang-fonts < 5.0-31
Provides: khmeros-battambang-fonts = %{version}-%{release}
}
%global fonts1            KhmerOS_battambang.ttf
%global fontconfs1        %{SOURCE1}
%global fontdescription1  %{expand:
%{common_description}

This package provides Battambang fonts.
}

%global fontfamily2       Bokor
%global fontsummary2      Bokor font
%global fontpkgheader2    %{expand:
Obsoletes: khmeros-bokor-fonts < 5.0-31
Provides: khmeros-bokor-fonts = %{version}-%{release}
}
%global fonts2            KhmerOS_bokor.ttf
%global fontconfs2        %{SOURCE2}
%global fontdescription2  %{expand:
%{common_description}

This package provides Bokor font family.
}

%global fontfamily3       Content
%global fontsummary3      Content font family
%global fontpkgheader3    %{expand:
Obsoletes: khmeros-base-fonts < 5.0-31
Provides: khmeros-base-fonts = %{version}-%{release}
}
%global fonts3            KhmerOS_content.ttf
%global fontconfs3        %{SOURCE3}
%global fontdescription3  %{expand:
%{common_description}

This package provides Content font family.
}

%global fontfamily4       Fasthand
%global fontsummary4      Fasthand font family
%global fontpkgheader4    %{expand:
Obsoletes: khmeros-handwritten-fonts < 5.0-31
Provides: khmeros-handwritten-fonts = %{version}-%{release}
}
%global fonts4            KhmerOS_fasthand.ttf
%global fontconfs4        %{SOURCE4}
%global fontdescription4  %{expand:
%{common_description}

This package provides Fasthand, a handwritten font family.
}

%global fontfamily5       Freehand
%global fontsummary5      Freehand font family
%global fontpkgheader5    %{expand:
Obsoletes: khmeros-handwritten-fonts < 5.0-31
Provides: khmeros-handwritten-fonts = %{version}-%{release}
}
%global fonts5            KhmerOS_freehand.ttf
%global fontconfs5        %{SOURCE5}
%global fontdescription5  %{expand:
%{common_description}

This package provides Freehand, a handwritten font family.
}

%global fontfamily6       Metal Chrieng
%global fontsummary6      Metal Chrieng font
%global fontpkgheader6    %{expand:
Obsoletes: khmeros-metal-chrieng-fonts < 5.0-31
Provides: khmeros-metal-chrieng-fonts = %{version}-%{release}
}
%global fonts6            KhmerOS_metalchrieng.ttf
%global fontconfs6        %{SOURCE6}
%global fontdescription6  %{expand:
%{common_description}

This package provides Metal Chrieng font.
}

%global fontfamily7       Muol
%global fontsummary7      Muol normal and Muol Light font family
%global fontpkgheader7    %{expand:
Obsoletes: khmeros-muol-fonts < 5.0-31
Provides: khmeros-muol-fonts = %{version}-%{release}
}
%global fonts7            KhmerOS_muol.ttf KhmerOS_muollight.ttf
%global fontconfs7        %{SOURCE7}
%global fontdescription7  %{expand:
%{common_description}

This package provides Muol normal and Muol Light font family.
}

%global fontfamily8       Muol Pali
%global fontsummary8      Muol Pali font
%global fontpkgheader8    %{expand:
Obsoletes: khmeros-muol-fonts < 5.0-31
Provides: khmeros-muol-fonts = %{version}-%{release}
}
%global fonts8            KhmerOS_muolpali.ttf
%global fontconfs8        %{SOURCE8}
%global fontdescription8  %{expand:
%{common_description}

This package provides Muol Pali font.
}

%global fontfamily9       Siemreap
%global fontsummary9      Siemreap font
%global fontpkgheader9    %{expand:
Obsoletes: khmeros-siemreap-fonts < 5.0-31
Provides: khmeros-siemreap-fonts = %{version}-%{release}
}
%global fonts9            KhmerOS_siemreap.ttf
%global fontconfs9        %{SOURCE9}
%global fontdescription9  %{expand:
%{common_description}

This package provides Siemreap fonts.
}

%global fontfamily10       System
%global fontsummary10      System font
%global fontpkgheader10    %{expand:
Obsoletes: khmeros-base-fonts < 5.0-31
Provides: khmeros-base-fonts = %{version}-%{release}
}
%global fonts10            KhmerOS_sys.ttf
%global fontconfs10        %{SOURCE10}
%global fontdescription10  %{expand:
%{common_description}

This package provides System font family.
}

Source0:        http://downloads.sourceforge.net/khmer/%{archivename}.zip
Source1:        68-%{fontpkgname1}.conf
Source2:        68-%{fontpkgname2}.conf
Source3:        68-%{fontpkgname3}.conf
Source4:        68-%{fontpkgname4}.conf
Source5:        68-%{fontpkgname5}.conf
Source6:        68-%{fontpkgname6}.conf
Source7:        68-%{fontpkgname7}.conf
Source8:        68-%{fontpkgname8}.conf
Source9:        68-%{fontpkgname9}.conf
Source10:       68-%{fontpkgname10}.conf
Source11:       License.txt

Name:      khmer-os-fonts
Summary:   Khmer font family set created by Danh Hong of the Cambodian Open Institute
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg -z 1,2,3,6,9,10

%global muolmetasummary All the Muol font family packages
%global muolmetadescription %{expand:
This meta-package installs all the Muol font family packages.
}

%global handwrittenmetasummary All the handwritten font family packages
%global handwrittenmetadescription %{expand:
This meta-package installs all the handwritten font family packages.
}
%fontmetapkg -n khmer-os-muol-fonts-all -s muolmetasummary -d muolmetadescription -z 7,8

%fontmetapkg -n khmer-os-handwritten-fonts -s handwrittenmetasummary -d handwrittenmetadescription -z 4,5

%prep
%oreon_verify_sources
%autosetup -n %{archivename}
install -p %{SOURCE11} .
%linuxtext License.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0-47
- Import
