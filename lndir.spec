Name: lndir
Version: 1.0.2
Release: %mkrel 4
Summary: Create a shadow directory of symbolic links to another directory tree
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-proto-devel
BuildRequires: pkgconfig

%description
The lndir program makes a shadow copy of a directory tree, except that
the shadow is not populated with real files but instead with symbolic links
pointing at the real files in the source directory tree. This is usually
useful for maintaining source code for different machine architectures. You
create a shadow directory containing links to the real source, which you will
have usually mounted from a remote machine. You can build in the shadow tree,
and the object files will be in the shadow directory, while the source files
in the shadow directory are just symlinks to the real files.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x 	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/lndir
%{_mandir}/man1/lndir.*



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2011.0
+ Revision: 666087
- mass rebuild

  + Paulo Ricardo Zanoni <pzanoni@mandriva.com>
    - Remove Packager tag

* Sun Sep 26 2010 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 581152
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-4mdv2010.1
+ Revision: 523190
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-2mdv2010.0
+ Revision: 426000
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-2mdv2009.0
+ Revision: 223120
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-1mdv2008.1
+ Revision: 129420
- kill re-definition of %%buildroot on Pixel's request
- do not hardcode bz2 extension


* Wed Dec 13 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.1-1mdv2007.0
+ Revision: 96296
- Added missing buildrequires
- adding lndir to the repository

