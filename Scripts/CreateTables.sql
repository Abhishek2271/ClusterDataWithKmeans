GO

/****** Object:  Table [dbo].[tbl_pj_SourceTypes]    Script Date: 08/02/2019 09:41:07 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[tbl_pj_SourceTypes](
	[TypeID] [int] IDENTITY(1,1) NOT NULL,
	[Type] [nvarchar](1000) NULL,
	[ReadInterval] [int] DEFAULT 1440,
PRIMARY KEY CLUSTERED 
(
	[TypeID] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

CREATE TABLE [dbo].[tbl_pj_SourceInfo](
	[SourceID] [int] IDENTITY(1,1) NOT NULL,
	[SourceName] [nvarchar](1000) NULL,
	[TypeID] [int] NULL,
	[URL] [nvarchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[SourceID] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[tbl_pj_SourceInfo]  WITH CHECK ADD FOREIGN KEY([TypeID])
REFERENCES [dbo].[tbl_pj_SourceTypes] ([TypeID])
GO

ALTER TABLE [dbo].[tbl_pj_SourceInfo]  WITH CHECK ADD FOREIGN KEY([TypeID])
REFERENCES [dbo].[tbl_pj_SourceTypes] ([TypeID])
GO

ALTER TABLE [dbo].[tbl_pj_SourceInfo]  WITH CHECK ADD FOREIGN KEY([TypeID])
REFERENCES [dbo].[tbl_pj_SourceTypes] ([TypeID])
GO



CREATE TABLE [dbo].[tbl_ex_RSSData](
	[ID] [bigint] IDENTITY(1,1) NOT NULL,
	[SourceID] [int] NULL,
	[Title] [nvarchar](2000) NULL,
	[Link] [nvarchar](2000) NULL,
	[Description] [nvarchar](max) NULL,
	[PublishedDate] [datetime] NULL,
	[UpdatedDate] [datetime] NULL,
	[ParsedDate] [datetime] NULL,
	[Hash] [nvarchar](80) NOT NULL,
	[Comments] [nvarchar](200) NULL,
	[Author] [nvarchar](80) NULL,
	[Category] [nvarchar](20) NULL,
	[Contributers] [nvarchar](2000) NULL,
PRIMARY KEY CLUSTERED 
(
	[Hash] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = ON, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
